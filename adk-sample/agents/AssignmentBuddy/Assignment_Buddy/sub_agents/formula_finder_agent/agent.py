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

"""Formula Finder Agent for identifying and explaining formulas based on input context."""

from google.adk import Agent

from . import prompt  # Define FORMULA_FINDER_PROMPT in prompt.py

# This agent does not use tools; it infers and explains formulas from context
formula_finder_agent = Agent(
    model='gemini-2.0-flash',
    name='formula_finder_agent',
    instruction=prompt.FORMULA_FINDER_PROMPT,
    tools=[],
)
