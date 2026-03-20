

async def scan_chat(chat_id):
    messages = await get_messages(chat_id)

    for msg in messages:
        if is_lead(msg):
            score = score_lead(msg)
            save_lead(msg, score)
