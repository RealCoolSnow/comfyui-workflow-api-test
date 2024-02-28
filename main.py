import json
import random
import time
from urllib import request, parse

from prompt import gen_prompt

# workflow = '/Users/coolsnow/code/ComfyUI/workflows/api/sdxl_lightning_workflow_full.json'
workflow = '/Users/coolsnow/code/ComfyUI/workflows/api/playground_v2.5.json'

positive_prompt = "Petra Collins, beautiful girl standing with beautiful vally in background, age 20, black short hair, waist shot, dynamic pose, smiling, dressed in fashion outfit, beautiful eyes, sweet makeup, 35mm lens, beautiful lighting, photorealistic, soft focus, kodak portra 800, 8k"

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


def test_sampler(sampler, scheduler):
    prompt = json.loads(prompt_text)
    prompt["6"]["inputs"]["text"] = positive_prompt
    prompt["9"]["inputs"]["filename_prefix"] = f"{sampler}-{scheduler}"
    # prompt["3"]["inputs"]["sampler_name"] = sampler
    # prompt["3"]["inputs"]["scheduler"] = scheduler
    prompt["3"]["inputs"]["seed"] = random.randint(0, 2 ** 32 - 1)
    queue_prompt(prompt)


def test_playground_v25(_positive_prompt):
    prompt = json.loads(prompt_text)
    prompt["6"]["inputs"]["text"] = _positive_prompt
    prompt["3"]["inputs"]["seed"] = random.randint(0, 2 ** 32 - 1)
    queue_prompt(prompt)


# KSAMPLER_NAMES = ["euler", "euler_ancestral", "heun", "heunpp2", "dpm_2", "dpm_2_ancestral",
#                   "lms", "dpm_fast", "dpm_adaptive", "dpmpp_2s_ancestral", "dpmpp_sde", "dpmpp_sde_gpu",
#                   "dpmpp_2m", "dpmpp_2m_sde", "dpmpp_2m_sde_gpu", "dpmpp_3m_sde", "dpmpp_3m_sde_gpu", "ddpm", "lcm"]
# SCHEDULER_NAMES = ["normal", "karras", "exponential", "sgm_uniform", "simple", "ddim_uniform"]
#
test_playground_v25(positive_prompt)
