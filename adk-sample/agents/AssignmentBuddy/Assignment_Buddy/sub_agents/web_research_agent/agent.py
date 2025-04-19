# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Web Research Agent for gathering verified facts and articles from the web."""

from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import google_search  # This will be used to fetch data from the web
from google.adk.models import LlmResponse

from . import prompt  # You can define WEB_RESEARCH_PROMPT in prompt.py

def _render_references(
    callback_context: CallbackContext,
    llm_response: LlmResponse,
) -> LlmResponse:
    """Appends references and sources to the response."""
    del callback_context  # Unused, but we have to include it for compatibility
    if (
        not llm_response.content or
        not llm_response.content.parts or
        not llm_response.grounding_metadata
    ):
        return llm_response
    references = []
    for chunk in llm_response.grounding_metadata.grounding_chunks or []:
        title, uri, text = '', '', ''
        if chunk.retrieved_context:
            title = chunk.retrieved_context.title
            uri = chunk.retrieved_context.uri
            text = chunk.retrieved_context.text
        elif chunk.web:
            title = chunk.web.title
            uri = chunk.web.uri
        parts = [s for s in (title, text) if s]
        if uri and parts:
            parts[0] = f'[{parts[0]}]({uri})'
        if parts:
            references.append('* ' + ': '.join(parts) + '\n')
    if references:
        reference_text = ''.join(['\n\nReference:\n\n'] + references)
        llm_response.content.parts.append(types.Part(text=reference_text))
    if all(part.text is not None for part in llm_response.content.parts):
        all_text = '\n'.join(part.text for part in llm_response.content.parts)
        llm_response.content.parts[0].text = all_text
        del llm_response.content.parts[1:]
    return llm_response


# This agent uses the google_search tool to fetch facts from the web
web_research_agent = Agent(
    model='gemini-2.0-flash',  # Replace with the appropriate model
    name='web_research_agent',
    instruction=prompt.WEB_RESEARCH_PROMPT,  # Define this prompt in your prompt.py file
    tools=[google_search],  # Using Google Search tool to gather facts
    after_model_callback=_render_references,  # Attach the references to the response
)
