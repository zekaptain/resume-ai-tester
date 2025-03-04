"""Test if resume is AI-parse-able."""
import os
import argparse
import logging
from core import ResumeParser


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pass_resume(pdf, model_name):
    """Pass the PDF to the OpenAI parser."""
    api_key = os.environ['OPENAI_API_KEY']
    # model = "gpt-4o-mini"

    parser = ResumeParser(api_key=api_key, model=model_name)
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
        "--model",
        default="gpt-4o-mini",
        help="Input the name of the AI model you want to use."
    )
    parser.add_argument(
        "--verbosity",
        default="INFO",
        choices=logging._nameToLevel.keys()
    )
    args = parser.parse_args()
    logger.setLevel(args.__dict__["verbosity"])
    fname = args.__dict__["file_name"]
    model = args.__dict__["model"]
    logger.info(
        {
            "input": fname,
            "model": model,
        }
    )
    pass_resume(fname, model)
