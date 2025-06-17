observation_id = 289864414

 from pyinaturalist import get_observations
 observation_id = 289864414 #Boletes
 response = get_observations(id=observation_id)
# print response  # to print out all observation parameters

# Display a more manageable list of parameters
if response and response.get('results'):
    observation = response['results'][0]  # There should only be one result for a specific ID
    print(f"Observation ID: {observation['id']}")
    print(f"Species: {observation['species_guess']}")
    print(f"Observed on: {observation['observed_on']}")
    print(f"Place: {observation['place_guess']}")
    print(f"User: {observation['user']['login']}")
    print(f"URL: {observation['uri']}")
else:
    print(f"Observation with ID {observation_id} not found or an error occurred.")

# Observation ID: 289864414
# Species: boletes
# Observed on: 2025-06-15 12:13:32-04:00
# Place: University Park, MD 20782, USA
# User: jmgconsult
# URL: https://www.inaturalist.org/observations/289864414