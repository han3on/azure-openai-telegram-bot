#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""ChatGPT Telegram Bot

Description to be added.

__author__ = han3on
__copyright__ = Copyright 2023
__version__ = 1.0.2
__maintainer__ = han3on
__email__ = bluehanson@gmail.com
__status__ = Dev
"""

import openai, json, os
import datetime
import logging
import signal
from config_loader import ConfigLoader
from logging_manager import LoggingManager

class OpenAIParser:

    # config_dict = {}

    def __init__(self):
        openai.api_type = ConfigLoader.get("openai", "api_type")
        openai.api_key = ConfigLoader.get("openai", "api_key")
        openai.api_base = ConfigLoader.get("openai", "api_base")
        openai.api_version = ConfigLoader.get("openai", "api_version")

    def _get_single_response(self, message):
        response = openai.ChatCompletion.create(engine = ConfigLoader.get("openai", "chat_model"),
                                                messages = [
                                                    {"role": "system", "content": "You are a helpful assistant"},
                                                    {"role": "user", "content": message}
                                                    ]
                                                )
        return response["choices"][0]["message"]["content"]
    
    def get_response(self, userid, context_messages):
        LoggingManager.debug("Get OpenAI GPT response for user: %s" % userid, "OpenAIParser")
        # context_messages.insert(0, {"role": "system", "content": "You are a helpful assistant"})
        try:

            def timeout_handler(signum, frame):
                raise Exception("Timeout")
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(int(ConfigLoader.get("openai", "api_timeout")))
            #### Timer ####
            response = openai.ChatCompletion.create(
                engine = ConfigLoader.get("openai", "chat_model"),
                messages = context_messages
                )
            ###############
            signal.alarm(0)
            return (response["choices"][0]["message"]["content"], response["usage"]["total_tokens"])
        except Exception as e:
            LoggingManager.error("OpenAI GPT request for user %s with error: %s" % (userid, str(e)), "OpenAIParser")
            return ("Oops, something went wrong with Azure OpenAI. Please try again later.", 0)

    def image_generation(self, userid, prompt):
        LoggingManager.debug("Get OpenAI Image Generation for user: %s" % userid, "OpenAIParser")
        response = openai.Image.create(prompt = prompt, n=1, size = "512x512", user = userid)
        image_url = response["data"][0]["url"]
        # for debug use
        # image_url = "https://catdoctorofmonroe.com/wp-content/uploads/2020/09/iconfinder_cat_tied_275717.png"
        usage = 1 # reserve for future use
        return (image_url, usage)

if __name__ == "__main__":
    openai_parser = OpenAIParser()
    # print(openai_parser._get_single_response("Tell me a joke."))
    print(openai_parser.get_response("123", [{"role": "system", "content": "You are a cat and only can say Meaw"}, {"role": "user", "content": "Say something to me."}]))
