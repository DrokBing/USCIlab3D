import sys
import requests
import json
# Define your API key here
api_key = ""

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}


text_query = 'I have some words, but some of them have similar meaning or refer to same object or it belongs to another words, help me merge all them as more as possible, Give me only all the final corresponding list, which has orignal words and corresponding words\n'
text_query += "'unlabeled', 'window', 'handrail', 'bench', 'sky', 'grass', 'door', 'wall', 'outdoor lighting', 'pipe', 'curb', 'brick wall', 'roof', 'tree', 'building', 'shrub', 'concrete', 'streetlight', 'pavement', 'door handle', 'stairs', 'shadow', 'pole', 'fence', 'person', 'lamp post', 'railing', 'bicycle', '##lch', 'potted plant', 'shrubbery', 'drain cover', 'light', 'gravel', 'cover', 'plant', 'lawn', 'umbrella', 'patio umbrella', 'table', 'chair', 'bush', 'planter', 'trash can', 'sidewalk', 'trash', 'parking lot', 'sign', 'vehicle', 'space line', 'portable toilet', 'van', 'parking space line', 'post', 'parking meter', 'path', 'ceiling', 'vegetation', 'banner', 'flower', 'lamp', 'bushes', 'reflection', 'outdoor furniture', 'street light', 'stone', 'outdoor seating', 'fountain', 'lighting', '##light', 'construction barrier', 'construction equipment', 'stop sign', 'truck', 'entrance', 'trash bin', 'street sign', 'hydrant', 'road', 'construction cone', 'bicycle racks', 'branch', 'red curb', 'brick', 'street', 'foliage', 'floor', 'plaque', 'pillar', '##rail', 'public art', 'gate', 'outdoor light', 'sun', 'plants', 'concrete wall', 'palm', 'palm tree', 'shrubs', 'balcony', 'balustrade', 'traffic cone', 'fire hydrant', 'bike rack', 'sunlight', 'chain', 'rock', 'glass', 'hedge', 'motorcycle', 'lamp posts', 'trailer', 'fencing', 'unit', 'soil', 'conditioning unit', 'bricks', 'air conditioning unit', 'driveway', 'pedestrian walkway', 'rocks', 'trash receptacle', 'parking bay marker', 'crosswalk', 'ramp', 'garden', 'handicap parking sign', 'ground', 'outdoor', 'flower bed', 'parking structure', 'signpost', 'solar panel', 'hand', 'pathway', 'pot', 'leaf', 'dumpster', 'manhole cover', 'paving stone', 'parking sign', 'construction site', 'road sign', 'golf cart', 'steps', 'potted', 'public seating', '‘', '‘ sign', '‘ stairs', 'railings', 'staircase', 'leaves', 'air unit', 'cart', 'vent', 'bin', 'recycling bin', 'windows', 'reflections', 'road marking', 'planters', 'billboard', '##ers', 'construction fence', 'chain - link', 'chain - link fence', '##ter', 'handicap parking symbol', 'parking symbol', 'electric box', 'symbol', 'signage', 'stair', 'air', 'cone', 'statue', 'sculpture', 'patio', 'doorway', 'space', 'house', 'lettering', 'walkway', 'portable', 'paved surface', 'parking space marker', 'bollard', 'metal fence', 'traffic light', 'graffiti', '##er', 'ventilation grill', 'scaffolding', 'cross', 'ceiling lights', 'air vent', 'cones', 'bus', 'hydra', 'public phone', 'construction cones', 'chain link fence', 'bay marker', 'greenery', 'plant pot', 'construction', 'container', 'exterior lighting', 'drainage grate', 'warning sign', 'canopy', 'garbage can', 'garbage', 'lot', 'rack', 'brickwall', 'air conditioner', '-', 'bus stop', 'parking curb', 'pedestrian crosswalk', 'shadows', 'flag', 'brickwork', 'gutter', 'doorhandle', 'recreational vehicle', 'parking bay', 'water', 'bike', 'ventilation grille', 'ceiling light', 'utility meter', 'metal gate', 'traffic bollard', 'curtain', 'paved stone', 'metal pole', 'emergency call station', 'utility pole', 'ladder', 'station', 'metal', 'glass reflection', '##bery', 'artificial lighting', 'painting', 'hedges', 'blue sky', 'trunk', 'tree trunk', 'blinds', 'clouds', 'stadium', 'pallet', 'pickup truck', 'yard', 'pebbles', 'interior lighting', 'rubble', 'advertisement', 'building exterior', 'human', 'seating', 'lights', 'lamppost', 'locker', 'cardboard box', 'trash bag', 'corridor', 'fire hydra', 'text', 'park bench', 'marker', 'ivy', 'outdoor gear', 'seat', 'car', 'vehicles', 'pedestrian', 'poster', '##ster', 'archway', 'clock tower', 'receptacle', 'parking', 'barrier', 'courtyard', 'flowers', 'mulch', 'poles', 'grass area', 'patio area', 'paved area', 'chairs', 'generator', 'tank', 'bulletin board', 'indoor seating', 'exit sign', 'garage', 'vending machine', 'machine', '##nding machine', 'handicap parking space', 'handicap space', 'lane marker', 'electrical box', 'column', 'equipment', 'branches', 'parking garage', 'rail', '##work', 'dump', 'construction materials', '##op', 'public bathroom', 'landscaping', 'lane', 'panel', 'traffic sign', 'bicycle rack', 'sports field', 'gates', 'emergency phone', 'scooter', 'paved walkway', 'road markings', 'board', 'notice board', 'flooring', '##nt', 'monument', 'art', 'concrete floor', 'security camera', 'twilight', 'signboard', 'lattice', 'camera', '##hole cover', 'waste container', 'ornament', 'base', 'golf', 'fire', 'handicap', 'letters', 'bicycles', '##hole', 'cement', 'advertising', 'ball', 'm lamp', 'architecture', 'girl', '##let', 'court', 'structure', 'flagpole', '##pole', 'arch', 'line', 'bleachers', 'step', 'emergency call', 'handle', '##post', 'traffic', 'skylight', 'walls', 'plaza', 'tennis court', 'netting', 'link fence', 'meter', 'surveillance camera', '##ry', 'asphalt', 'red', '##rade', 'hat', 'transportation sign', 'architectural column', 'public bench', 'emergency vehicle', 'emergency', 'baseball field', 'concrete flooring', 'flowerbed', '##folding', '‘ staircase', 'i', 'handicap symbol', 'stop', 'man cover', 'humans', 'plaques', 'construction material', 'pavement markings', 'cargo container', 'call', 'boy', 'space marker', 'trees', 'people', 'parking space', 'tile', 'tennis', 'chain fence', 'intersection', 'stick symbol', 'walking stick symbol', '‘ handrail', '‘ lamp post', '‘ road', 'buildings', 'shub', 'signs', 'streetlights', 'doors', 'handicap parking', 'birds', 'case', 'stair case', 'bottle', 'awning', 'cloud', 'indoor lighting', 'rooftop', 'electric', 'tent', 'chain - fence', 'number', 'blue light', 'chain link', 'metal railing', 'rope', 'bricklines', 'roadway', 'green area', 'exterior', 'public space', 'campus', 'closed sign', 'bal', 'mailbox', 'bus stop shelter', 'stairway', 'field', 'curve', 'bod', 'rental bikes', 'streetsign', 'tire', 'wheels', 'dirt', 'iron', 'call station', 'conditioner', 'grassy area', 'shade', 'bay', 'pipeline', 'bag', '‘ chair', 'm', 'backpack', 'indoor light', 'bed', 'planting bed', 'lamps', 'picnic table', 'park', 'insulation', 'trash container', 'barricade', 'red _ curb', 'picnic _ table', 'brick _ wall', 'construction _ equipment', 'hallway', 'frame', 'public sign', 'firent', 'power generator', 'garden bed', 'box', 'pal', 'statues', 'posts', 'reserved parking sign', 'exit', 'female toilet symbol', 'racks', 'landscape', 'stump', 'furniture', 'advertising board', 'concrete planter', 'balrade', 'parapet wall', 'handicap sign', 'vase', 'man', 'chain -', 'pickup', '‘ lamp', 'brick walkway', 'bollar', 'baseball', 'bucket', 'image', 'security', 'the image', 'bike _ rack', 'security _ camera', 'windowpane', 'reservation sign', 'rec', 'lanes', 'roofing', 'door knob', 'scene the image', 'street signs', 'brick paving', 'empty space', 'information sign', 'sports', '##walk', '##leachers', 'bo', 'public', 'perimeter fence', '##ust', 'piping', 'flowering plants', 'paving', 'grill', 'torch', 'net', 'pipes', 'bus shelter', 'porch', 'recacle', 'bikes', 'cable', 'tables', 'mu', 'basin', 'trash recacle', 'pavilion', 'materials', 'lighting equipment', 'balust', '##ree', 'streelight', 'pip', '##d', '‘ building', '‘ tree', '‘ bench', '##llar', 'utility', 'stlight', 'gut', 'rental', 'skateboard', 'st', 'manhole', '##llard', '##lights', 'pot plant', 'wood', 'toilet', 'railway', 'golf course', 'reservoir', 'feeding station', 'elevator', 'valve', 'phone', 'construction _ barrier', 'scfolding', 'trash recept', 'lantern', '- fence', 'trash _ bin', '_ rack', 'grass _ patch', 'plastic', 'debris', 'paved', 'cardboard', 'barrica', 'grass patch', 'patch', 'pedestrian cross', 'trash _', '##ted', '##icade', 'trash _ can', '##ustrade', 'grate', 'blea', '- link', 'stroller', 'trashacle', 'trashept', '##ing', 'barr', 'construction _ site', 'drainage', 'ventilation', 'trash rec', '- link fence'"
payload = {
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": text_query
                }
            ]
        }
    ],
}
print('??')
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# Handle the response here
print(response.json())


with open('./sam2.txt', 'w') as f:
    json.dump(response.json(), f)
