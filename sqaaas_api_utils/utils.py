# SPDX-FileCopyrightText: Copyright contributors to the Software Quality Assurance as a Service (SQAaaS) project.
# SPDX-FileContributor: 2017-2024 Pablo Orviz <orviz@ifca.unican.es>
#
# SPDX-License-Identifier: GPL-3.0-only


import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("sqaaas-step-action")


TOOLING_URL = "https://raw.githubusercontent.com/EOSC-synergy/sqaaas-tooling/release/2.0.0/tooling.json"


def get_tool_data(tool, lang):
    """Return tool data from the SQAaaS tooling.

    Keyword arguments:
    tool -- the tool to get the tooling arguments from
    lang -- the language that the tool is mapped to
    """
    logger.debug("Using SQAaaS tooling metadata: %s" % TOOLING_URL)
    req = requests.get(url=TOOLING_URL)
    data = req.json()

    return data["tools"][lang][tool]
