import json
from urllib import request, parse

from prompt import gen_prompt

# 读取文件全部内容
workflow = '/Users/coolsnow/code/ComfyUI/workflows/api/sdxl_lightning_workflow_full.json'
with open(workflow, 'r') as f:
    prompt_text = f.read()


def queue_prompt(prompt):
    p = {"prompt": prompt}
    print(f"queue prompt: {p}")
    data = json.dumps(p).encode('utf-8')
    req = request.Request("http://127.0.0.1:8188/prompt", data=data)
    resp = request.urlopen(req)
    print("response:", resp.read().decode('utf-8'))


def test_gen_prompt():
    prompt = json.loads(prompt_text)
    # set the text prompt for our positive CLIPTextEncode
    new_prompt = gen_prompt()
    # print(f'prompt: {new_prompt}')
    prompt["6"]["inputs"]["text"] = new_prompt

    # set the seed for our KSampler node
    # prompt["3"]["inputs"]["seed"] = 5

    queue_prompt(prompt)

# 循环遍历100次
for i in range(100):
    test_gen_prompt()