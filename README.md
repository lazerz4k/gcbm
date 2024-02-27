# GCBM
_**G**enerative **C**onversation **B**etween **M**odels_

A tool/framework for conversations and interactions between multiple AI models at once.

This framework can be used to engage in, develop with, or converse with multiple models in one continous conversation with the same context.

Currently, the source code uses two GPT-4 models, this framework can be restructured to use more models by OpenAI or even other models like Google's Gemini.

# Prerequisites

The ```main.py``` file currently uses the OpenAI Python API Library.

To install the dependencies, open your terminal and run the following:

```pip install openai```

*You also need an OpenAI API key. Unfortunately, you can't run the program unless you have a bit of credit in your OpenAI account.*

# Setup

Before running, open the text editor of your choice, and input your OpenAI API key.

And afterwards, change the AI prompts for each AI model you wish to use.

In the source code, there are currently two initial prompts in the lists ```conversation1``` and ```conversation2```

You can change them according to the personality or character you wish the AI should inhabit.

# How to use it

Ultimately, you should have fun with this tool, or brainstorm ideas with it, or maybe make it a double co-pilot! The possibilites are endless, I made this as a helping hand for people trying to become more productive, but you do you!

You can use this framework for a variety of things! Have fun building something with this, or maybe just playing around.

# Before continuing...

Although the GNU GPL states that you can do whatever you want with the source code, I highly recommend NOT to add NSFW prompts for the models, you can get your OpenAI developer account banned, the same might go for the maintainers for the other AI models if you wish to add them.

Furthermore, your prompts and the conversations between the models can be viewed by OpenAI _(If you use GPT)_. This is mentioned in their privacy policy, hence please don't share sensitive information _(Unless you are eligible for Zero Retention, then they wont keep any data)_. The same probably goes for other AI model maintainers.
