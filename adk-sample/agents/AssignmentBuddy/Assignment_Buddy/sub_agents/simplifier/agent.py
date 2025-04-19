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

"""Simplifier agent for rewriting complex answers into easy explanations."""

from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse

from . import prompt

_END_OF_SIMPLIFICATION_MARK = '---END-OF-SIMPLIFICATION---'

def _clean_simplified_response(
    callback_context: CallbackContext,
    llm_response: LlmResponse,
) -> LlmResponse:
    del callback_context  # unused
    if not llm_response.content or not llm_response.content.parts:
        return llm_response
    for idx, part in enumerate(llm_response.content.parts):
        if _END_OF_SIMPLIFICATION_MARK in part.text:
            del llm_response.content.parts[idx + 1 :]
            part.text = part.text.split(_END_OF_SIMPLIFICATION_MARK, 1)[0]
    return llm_response


simplifier_agent = Agent(
    model='gemini-2.0-flash',
    name='simplifier_agent',
    instruction=prompt.SIMPLIFIER_PROMPT,
    after_model_callback=_clean_simplified_response,
)
