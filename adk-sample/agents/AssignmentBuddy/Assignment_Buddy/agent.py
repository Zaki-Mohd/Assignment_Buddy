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

"""Assignment Buddy: An assistant that solves and simplifies academic queries for students."""

from google.adk.agents import SequentialAgent

from .sub_agents.solver import solver_agent
from .sub_agents.simplifier import simplifier_agent
from .sub_agents.web_research_agent import web_research_agent
from .sub_agents.formula_finder_agent import formula_finder_agent
from .sub_agents.quiz_maker_agent import quiz_maker_agent

assignment_buddy = SequentialAgent(
    name='assignment_buddy',
    description=(
        'An all-in-one assistant for students. It solves questions, simplifies concepts, '
        'adds web-researched facts, suggests relevant formulas, and creates practice quizzes.'
    ),
    sub_agents=[
        solver_agent,
        simplifier_agent,
        web_research_agent,
        formula_finder_agent,
        quiz_maker_agent,
    ],
)

root_agent = assignment_buddy
