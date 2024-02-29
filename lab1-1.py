import requests                                                 #Εισαγωγή βιβλιοθήκης Requests

url=input("Please, enter URL:")                                 #Αιτούμαι URL από το χρήστη      
url1=url.strip(' ')                                              #Αφαιρώ τα κενά από αρχή και τέλος

if not url1.startswith("http://"):                              #Ελέγχω αν το URL μου έχει http:// μπροστά
    url1="http://"+url1                                         #Όταν δεν έχει, το προσθέτω

with requests.get(url1) as response:                            #Δημιουργώ το αντικείμενο response μετά από αίτημα http
    print(f"Headers of {url1}, are: {response.headers}\n")    	#Τυπώνω τις κεφαλίδες του αιτήματος http

    url1_server=response.headers.get('Server')                  #Βρίσκω το λογισμικό που χρησιμοποιεί ο server 
    if url1_server:                                             #Ελέγχω αν υπάρχει 
        print(f"The software used by the server is: {response.headers.get('Server')}\n")
    else:
        print("No server detected.")                            #Εκτύπωση σε περίπτωση μη ύπαρξης

    cookies_text=response.cookies                               #Δημιουργώ αντικείμενο που περιέχει τα Cookies 
    if cookies_text:                                            #Ελέγχω αν υπάρχουν Cookies   
        for cookie in cookies_text:                             #Αν υπάρχουν, παίρνω το όνομα κάθε Cookie και το διάστημα για το οποίο θα είναι έγκυρο
            print(f"Cookie Name:{cookie.name}, Expiry time:{cookie.expires}")
    else: print("There are no cookies used.")

#Δοκίμασα πολλά URL (πχ youtube, eclass) και στο ένα ο κώδικας λειτουργεί κανονικά ενώ στο άλλο εμφανίζει ένα error που δεν μπόρεσα να 
#καταλάβω από που προέρχεται. Επίσης, το expires δίνει χρόνο σε δευτερόλεπτα αλλά ούτε αυτό κατάφερα να επιλύσω. Κάποια πιθανή διόρθωση;