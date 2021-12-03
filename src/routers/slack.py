from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..config import config
from ..logging import log
import requests
import json


router = APIRouter(prefix="/slack", tags=["slack"])


class SlackMessage(BaseModel):
    message: str


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Aruba notify",
}


@router.post("/")
async def notification_via_slack(message: SlackMessage):
    """Send a webhook notification to a slack channel"""
    data = {}
    url = f"{config.SLACK_URL}{config.SLACK_TOKEN}"
    data["text"] = message.message
    data = json.dumps(data)
    try:
        requests.post(url=url, headers=headers, data=data, timeout=90)
        resposne = {"message": "Sent to slack"}
        log.info(resposne)
        return resposne
    except requests.exceptions.ReadTimeout as e:
        log.warning("Did a time out: {}".format(e))
        raise HTTPException(
            status_code=418,
            detail="Time out to slack. Notification was not sent.",
        )
