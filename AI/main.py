from openai import OpenAI
import asyncio

client = OpenAI(
    api_key="" 
)


async def generate_avatar(description):
    response = await client.images.generate(
        model="dall-e-3",
        prompt=description,
        size="1024x1024",
        n=1,
    )
    return response.data[0].url

# Описи для кожного персонажа
descriptions = {
    "Мафія": "Аватар для гри у комікс-стилі. Може бути чоловіком або жінкою в чорному костюмі, з капелюхом та сонцезахисними окулярами, з загрозливим виразом обличчя.",
    "Шериф": "Аватар шерифа, що виглядає сміливо та справедливо. Може мати пістолет на стегні, знак шерифа на грудях та виразніми рисами обличчя.",
    "Лікар": "Представлення лікаря у комікс-стилі. Вбрання в білий халат або медичну уніформу, можливо з медичним набором у руках та доброзичливим виразом обличчя.",
    "Мирний житель": "Звичайна людина у комікс-стилі, без характерних ознак інших персонажів. Може мати доброзичливий вираз обличчя та повсякденне вбрання."
}

async def generate_avatars():
    avatars = {}
    for role, description in descriptions.items():
        avatars[role] = await generate_avatar(description)
    return avatars

async def main():
    avatars = await generate_avatars()
    for role, avatar_url in avatars.items():
        print(f"Аватар для {role}: {avatar_url}")

asyncio.run(main())