# SPDX-FileCopyrightText: Copyright contributors to the Software Quality Assurance as a Service (SQAaaS) project.
# SPDX-FileContributor: 2017-2024 Pablo Orviz <orviz@ifca.unican.es>
#
# SPDX-License-Identifier: GPL-3.0-only


import logging
import requests


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


def run_assessment(repo, branch=None, step_tools=[]):
    pipeline_id = None
    action = "create"
    sqaaas_report_json = {}

    wait_period = 5
    keep_trying = True
    while keep_trying:
        logger.info(f"Performing {action} on pipeline {pipeline_id}")
        if action in ["create"]:
            payload = json.loads(create_payload(repo, branch, step_tools))
            logging.debug("Using payload: %s" % payload)
            response = sqaaas_request("post", "pipeline/assessment", payload=payload)
            response_data = response.json()
            pipeline_id = response_data["id"]
            action = "run"
        elif action in ["run"]:
            response = sqaaas_request("post", f"pipeline/{pipeline_id}/{action}")
            action = "status"
        elif action in ["status"]:
            response = sqaaas_request("get", f"pipeline/{pipeline_id}/{action}")
            response_data = response.json()
            build_status = response_data["build_status"]
            if build_status in COMPLETED_STATUS:
                action = "output"
                logging.info(
                    f"Pipeline {pipeline_id} finished with status {build_status}"
                )
            else:
                time.sleep(wait_period)
                logger.info(
                    f"Current status is {build_status}. Waiting {wait_period} seconds.."
                )
        elif action in ["output"]:
            keep_trying = False
            response = sqaaas_request(
                "get", f"pipeline/assessment/{pipeline_id}/{action}"
            )
            sqaaas_report_json = response.json()

    return sqaaas_report_json
