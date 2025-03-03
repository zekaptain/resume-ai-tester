# A simple python wrapper for PDF parsing with OpenAI
### **With a focus on resumes/CVs**

## TL;DR

Check if your resume is parse-able by AI resume parsers that utilize LLMs.

Since I wanted to test my own resume for AI parse-ibility, I decided to write a little python wrapper. Since the OpenAI API was updated, the one [pip package](https://github.com/resumeupai/resume-parser-ai) I could find to do this no longer works.

I have updated the `resumeupai` code to work with *OpenAI Python v1.65.2*.

## To use:

First, open your terminal and `cd` into the folder where this code exists.

Once there, you can export your OpenAI API key and call the `personal-resume-parser.py` script, like so:

```
export OPENAI_API_KEY="your-API-key-goes-here"
python personal-resume-parser.py --file_name "/Path/To/Resume.pdf"
```

The output will be printed to your terminal in JSON format. Check the key:value pairs for accuracy by comparing to your input PDF.