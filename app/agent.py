from dotenv import load_dotenv
load_dotenv()

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent


@tool
def get_trending_topics(platform: str) -> str:
    """Get trending topics for a given social media platform.
    Use this when the user asks about what content is currently popular."""
    return f"Trending topics for {platform}: AI art, productivity tips, behind-the-scenes content"


@tool
def get_content_ideas(niche: str) -> str:
    """Get content format ideas for a given niche or topic.
    Use this when the user asks for content ideas, formats, or creative suggestions."""
    return (
        f"Content ideas for {niche}: "
        "1) Carousel post — break down a common myth in your niche into 5 slides. "
        "2) Reel — show a before and after transformation in 30 seconds. "
        "3) Story series — share 3 quick tips over 3 consecutive days. "
        "4) Long-form video — do a full tutorial or deep dive on a topic your audience keeps asking about."
    )


@tool
def get_hashtags(niche: str) -> str:
    """Get relevant hashtags for a given niche or topic.
    Use this when the user asks for hashtags, tags, or ways to increase reach."""
    return (
        f"Top hashtags for {niche}: "
        f"#{niche.replace(' ', '')} #ContentCreator #GrowYourAudience "
        "#Viral #Trending #CreatorTips #SocialMediaMarketing #ContentStrategy"
    )


tools = [get_trending_topics, get_content_ideas, get_hashtags]

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"],
)

system_prompt = (
    "You are AlgoRhythm, a content creator assistant. "
    "You help creators plan posts, choose hashtags, and identify trending topics. "
    "Use your tools when the user asks about trends, platform-specific content, or content format ideas."
)

agent = create_react_agent(model, tools, prompt=system_prompt)
