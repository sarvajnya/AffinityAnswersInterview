import requests

def verify_pincode(address):
    
    pincode = ''
    
    for i in address.split():
        if i.isdigit() and len(i) == 6:
            pincode = i
            break
    
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
                    return True #Valid
            
    return False #Invalid