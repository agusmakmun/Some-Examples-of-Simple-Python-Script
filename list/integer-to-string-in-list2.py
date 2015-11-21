def ganti_variable(inputan):
    _split = inputan.split("\n")
    for item in _split:
        if item == '':
            pass
        else:
            join = ' '.join(item)
            mapping = map(int, join.split())
            listing = [ p*"X" for p in mapping if p%2 != 0 and p > 2 and p !=9 or p == 2]
            #print listing
            if len(listing) == 0:
                pass
            else:
                char_replace = ["[", "]", ",", "'"]
                print str(listing).translate(None, ''.join(char_replace))
            
inputan = """
468557
468647
468719
468841
468913
469099
469229
469331
469439
469589
469717
469811
469939
470081
470179
470263
470389
470461
"""
ganti_variable(inputan)




#OUTPUT:
XXXXX XXXXX XXXXXXX                                                                                                                                          
XXXXXXX                                                                                                                                                      
XXXXXXX                                                                                                                                                      
XXX                                                                                                                                                          
XX XX                                                                                                                                                        
XXX XXX                                                                                                                                                      
XXX                                                                                                                                                          
XXXXX                                                                                                                                                        
XXXXXXX XXXXXXX                                                                                                                                              
XXX                                                                                                                                                          
XXXXXXX                                                                                                                                                      
XXXXXXX XXXXXXX                                                                                                                                              
XXXXXXX XX XXX                                                                                                                                               
XXXXXXX XXX                                                                                                                                                  
XXXXXXX
