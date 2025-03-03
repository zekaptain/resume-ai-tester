"""Test if resume is AI-parse-able."""
import os
import argparse
import logging
from core import ResumeParser


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pass_resume(pdf):
    """Pass the PDF to the OpenAI parser."""
    api_key = os.environ['OPENAI_API_KEY']
    model = "gpt-4o-mini"

    parser = ResumeParser(api_key=api_key, model=model)
    resume_data = parser.parse(pdf)

    print(resume_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file_name",
        default="resume.pdf",
        help="Input filepath and name of resume"
    )
    parser.add_argument(
        "--verbosity",
        default="INFO",
        choices=logging._nameToLevel.keys()
    )
    args = parser.parse_args()
    logger.setLevel(args.__dict__["verbosity"])
    fname = args.__dict__["file_name"]
    logger.info(
        {
            "input": fname,
        }
    )
    pass_resume(fname)
