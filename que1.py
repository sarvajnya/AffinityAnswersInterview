import requests

def verify_pincode(address):
    global pincode
    
    pincode = address.split()[-1] # Get PIN Code from input address which is at last index
    
    # Get the correct address from the given PIN code
    api_url = f"https://api.postalpincode.in/pincode/{pincode}"
    response = requests.get(api_url)
    
    if response.status_code == 200: #Valid response
        data = response.json()
        
        if data[0]['Status'] == 'Success':
            
            for i in range(len(data[0]['PostOffice'])) :
                
                correct_postal_address = data[0]['PostOffice'][i]['Name']
                correct_pincode = data[0]['PostOffice'][i]['Pincode']
                
                
                # Compare the correct PIN code with the provided PIN code and check for correct postal address
                if correct_pincode == pincode and correct_postal_address in address:
                    return True
            
    return False #Invalid

# Test cases
# Free flowing address as input
test_cases = [
    '''2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050''', #Valid address
    '''2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050''', #Valid address
    '''374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore, 560050''', #Valid address
    '''2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095''', #Invalid address
    '''Colony, Bengaluru, Karnataka 560050''', #Invalid address
]

for address in test_cases:
    if verify_pincode(address) :
        print(f"Address: '{address}' has the correct PIN code: '{pincode}'")
    else:
        print(f"Address: '{address}' is incorrect")
