from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import FileResponse
from backend.src.util import Extract
import uvicorn

app = FastAPI()


@app.post("/extract_data")
async def extract_data(file: UploadFile = File(),
                       file_format: str = Form()):
    contents = file.file.read()
    with open("../upload/test.pdf", "wb") as f:
        f.write(contents)
        data = Extract("../upload/test.pdf", file_format).extract_text()
    return data

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
