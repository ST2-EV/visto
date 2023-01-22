import json
from moodpicker import pick_mood
from imgen import generate_image

def create_schema(script, character_map):
    schema = []
    lineSchema=None
    char_map_images = {}
    for char in character_map:
        char_map_images[char] = generate_image(character_map[char], 'char')
    for line in script:
        if line[0] == 'bg':
            if lineSchema is not None:
                schema.append(lineSchema)
            lineSchema={'characters':[]}
            lineSchema['bg'] = generate_image(line[1], 'bg')
        elif line[0] == 'mood':
            lineSchema['tone'] = pick_mood(line[1])
        elif line[0] == 'Narrator' or line[0] == 'narrator':
            lineSchema['characters'].append({
                "name": 'Narrator',
                "dialogue": line[1]
            })
        else:
            print(line[0])
            lineSchema['characters'].append({
                "name": line[0],
                "dialogue": line[1],
                "image": char_map_images[char]
            })
    schema.append(lineSchema)
    return schema

if __name__ == "__main__":
    script = [('bg', 'Long-Lost Wood is a dense forest with tall, leafy trees and winding paths. It is filled with puddles, and the air is often filled with the sound of the wind whistling through the trees.'), ('mood', 'adventure music'), ('Narrator', 'At one end of Long-Lost Wood, where the Wise Owl watched out for wolves, there lived a little girl. Whenever the wind whistled she wore a warm, scarlet cloak, so the animals called her Little Red Riding Hood.'), ('Mother', 'You must take this basket of sweet cherry pies to Grandma’s house. Follow the twisty path, jump the puddles and NEVER speak to the Big Bad Wolf.'), ('Little Red Riding Hood', 'OK, Mother. I will be careful.'), ('bg', 'The setting of the story is a forest with winding trails and puddles, bramble bushes, and tall, dark shadows from the trees. The end of the journey is a small cottage with a green door at the other end of Long-Lost Wood.'), ('mood', 'mystery music'), ('    Narrator', 'Little Red Riding Hood skipped away. She followed the twisty path and jumped over the puddles until she came to a bramble bush.'), ('Little Red Riding Hood', 'Oh no! A thorn spiked her scarlet cloak and held her tight.'), ('Narrator', '“Keep still, my dear,” boomed a deep voice. “I’ll soon set you free.” Sure enough, the thorn snapped, the cloak flapped and Little Red Riding Hood swung around.'), ('Little Red Riding Hood', '“Thank you,” she cried, but all she could see was a tall dark shape, standing in the shadows.'), ('Narrator', '“Where are you walking to, all alone?” it asked, in its deep, booming voice. Little Red Riding Hood thought she caught a glimpse of big eyes and sharp teeth.'), ('Little Red Riding Hood', '“To Grandma’s house,” answered Little Red Riding Hood nervously. “She lives at the other end of Long-Lost Wood, in the cottage with a green door.”'), ('Narrator', 'At that moment an owl hooted and the dark shape was gone, melting into the trees. Little Red Riding Hood didn’t know she had just met the Big Bad Wolf, so she just wandered along happily, singing tunes to herself.'), ('bg', 'The story takes place in a cozy cottage surrounded by lush green trees and a meandering path. The cottage has a bright green door and a chimney billowing smoke. A white picket fence encircles the house and a small garden is visible in the front.'), ('mood', 'mystery music'), ('    Narrator', 'Meanwhile, the hungry wolf raced to Grandma’s house and knocked on her green door.'), ('Wolf', '"Let me in, Grandma,” he said in his squeakiest voice. “I have brought you a basket of sweet cherry pies.”'), ('Grandma', 'But did Grandma put on her two pointy shoes and let him in? I’m afraid that she did! Poor Grandma.'), ('Narrator', 'And poor Little Red Riding Hood, who reached the cottage far too late.'), ('Little Red Riding Hood', '“Let me in, Grandma,” she called merrily. “I have brought you a basket of sweet cherry pies.”'), ('Grandma', '“Let yourself in, my dear,” replied a croaky voice. “I am in bed with a nasty cold.”'), ('bg', 'The room was dark and cozy, with a wooden floor and walls lined with shelves full of books. A large, four-poster bed stood in the center of the room, with a small nightstand next to it. A fireplace was in the corner, its embers still glowing from the fire that had been burning earlier.'), ('mood', 'mystery music'), ('Narrator', "Little Red Riding Hood lifted the latch and stepped inside. Someone was tucked up in bed wearing Grandma's favorite nightcap. The room was dark, so Little Red Riding Hood crept closer."), ('Little Red Riding Hood', '"Grandma," she whispered. "What big eyes you\'ve got."'), ('Grandma', '"All the better to see you with," said the voice.'), ('Narrator', 'With a sneeze, their nightcap fell off!'), ('bg', 'The story takes place in a small cottage in the middle of a dense forest. The room is dark and filled with shadows, lit only by the faint flicker of a small candle. The walls are made of wooden logs, and the floor is covered in a thick layer of dust. A large bed sits in the corner, with a large gray wolf lying atop it.'), ('mood', 'horror music'), ('Narrator', '"Grandma," gasped Little Red Riding Hood. "What big ears you\'ve got."'), ('Little Red Riding Hood', '"Grandma, what big teeth you\'ve got."'), ('Wolf', '"All the better to hear you with," growled the voice.  "All the better to eat you with," roared the voice.'), ('Little Red Riding Hood', '"Wait! You\'re not my grandma!"'), ('Narrator', 'The wolf sprang out of the bed, its sharp teeth flashing in the dark.'), ('Wolf', '"And that\'s why you should never stop and speak to the Big Bad Wolf!"'), ('bg', 'The story takes place in a small cottage on the edge of a vibrant forest. The cottage is surrounded by tall trees and lush green shrubbery. Inside, the walls are painted a bright red, and the floor is covered with a plush rug. There is a small wooden door leading out to the garden, and a large window looking out onto the forest.'), ('mood', 'comedy music'), ('Narrator', "Little Red Riding Hood saw the Wolf's fat tummy and screamed for help."), ('Little Red Riding Hood', 'Help, help! The Big Bad Wolf has eaten my Grandma and he wants to eat me too!'), ('Narrator', 'Luckily, the Wise Owl had already sent for the Storyland Vets.'), ('Narrator', 'The Vets burst through the green door with their magic medicine and in no time the Wolf was fast asleep.'), ('Narrator', 'Inside his tummy, they found Grandma safe and well, but when they sewed him up again they accidentally left her two pointy shoes inside!'), ('Narrator', 'So now, whenever the Wolf feels hungry, those two shoes dance and prance until he howls – and that is why he never even dreams of eating a grandma again.')]
    character_map = {'Mother': ' The mother was a tall woman with curly brown hair and brown eyes. She was wearing a long green dress with a white apron.', 'Little Red Riding Hood': ' Little Red Riding Hood was a small girl with long, curly red hair and bright blue eyes. She was wearing a red cape with a hood, a white dress, and a basket of food in her hands.', 'Big Bad Wolf': ' The Big Bad Wolf is a tall, dark figure with sharp eyes and teeth. He is menacing and intimidating, but his voice has a deep, booming tone.', 'Grandma': ' Grandma was an elderly woman with white hair and kind eyes. She was wearing a colorful dress with a white apron and a red shawl.', 'Wolf': ' The wolf was a large, grey animal with sharp claws and teeth. He had a big, bushy tail and yellow eyes that glowed in the dark.'}
    print(json.dumps(create_schema(script, character_map), indent=4))