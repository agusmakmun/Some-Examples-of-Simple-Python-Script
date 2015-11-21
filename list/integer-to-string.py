def ganti_variable(inputan):
    _split = inputan.split("\n")
    for item in _split:
        if item == '':
            pass
        else:
            join = ' '.join(item)
            mapping = map(int, join.split())
            listing = [ p*"X" for p in mapping ] #or: [ p*"X" for p in mapping if p%2 != 0 and p > 2]  --> cond prime.
            print listing
            
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


#Output:
['XXXX', 'XXXXXX', 'XXXXXXXX', 'XXXXX', 'XXXXX', 'XXXXXXX']                                                                                                  
['XXXX', 'XXXXXX', 'XXXXXXXX', 'XXXXXX', 'XXXX', 'XXXXXXX']                                                                                                  
['XXXX', 'XXXXXX', 'XXXXXXXX', 'XXXXXXX', 'X', 'XXXXXXXXX']                                                                                                  
['XXXX', 'XXXXXX', 'XXXXXXXX', 'XXXXXXXX', 'XXXX', 'X']                                                                                                      
['XXXX', 'XXXXXX', 'XXXXXXXX', 'XXXXXXXXX', 'X', 'XXX']                                                                                                      
['XXXX', 'XXXXXX', 'XXXXXXXXX', '', 'XXXXXXXXX', 'XXXXXXXXX']                                                                                                
['XXXX', 'XXXXXX', 'XXXXXXXXX', 'XX', 'XX', 'XXXXXXXXX']                                                                                                     
['XXXX', 'XXXXXX', 'XXXXXXXXX', 'XXX', 'XXX', 'X']                                                                                                           
['XXXX', 'XXXXXX', 'XXXXXXXXX', 'XXXX', 'XXX', 'XXXXXXXXX']                                                                                                  
['XXXX', 'XXXXXX', 'XXXXXXXXX', 'XXXXX', 'XXXXXXXX', 'XXXXXXXXX']                                                                                            
['XXXX', 'XXXXXX', 'XXXXXXXXX', 'XXXXXXX', 'X', 'XXXXXXX']                                                                                                   
['XXXX', 'XXXXXX', 'XXXXXXXXX', 'XXXXXXXX', 'X', 'X']                                                                                                        
['XXXX', 'XXXXXX', 'XXXXXXXXX', 'XXXXXXXXX', 'XXX', 'XXXXXXXXX']                                                                                             
['XXXX', 'XXXXXXX', '', '', 'XXXXXXXX', 'X']                                                                                                                 
['XXXX', 'XXXXXXX', '', 'X', 'XXXXXXX', 'XXXXXXXXX']                                                                                                         
['XXXX', 'XXXXXXX', '', 'XX', 'XXXXXX', 'XXX']                                                                                                               
['XXXX', 'XXXXXXX', '', 'XXX', 'XXXXXXXX', 'XXXXXXXXX']                                                                                                      
['XXXX', 'XXXXXXX', '', 'XXXX', 'XXXXXX', 'X'] 


Output2, prime:
['XXXXXXX']                                                                                                                                                  
['XXXXXXX', 'XXXXXXXXX']                                                                                                                                     
[]                                                                                                                                                           
['XXXXXXXXX', 'XXX']                                                                                                                                         
['XXXXXXXXX', 'XXXXXXXXX', 'XXXXXXXXX']                                                                                                                      
['XXXXXXXXX', 'XXXXXXXXX']                                                                                                                                   
['XXXXXXXXX', 'XXX', 'XXX']                                                                                                                                  
['XXXXXXXXX', 'XXX', 'XXXXXXXXX']                                                                                                                            
['XXXXXXXXX', 'XXXXX', 'XXXXXXXXX']                                                                                                                          
['XXXXXXXXX', 'XXXXXXX', 'XXXXXXX']                                                                                                                          
['XXXXXXXXX']                                                                                                                                                
['XXXXXXXXX', 'XXXXXXXXX', 'XXX', 'XXXXXXXXX']                                                                                                               
['XXXXXXX']                                                                                                                                                  
['XXXXXXX', 'XXXXXXX', 'XXXXXXXXX']                                                                                                                          
['XXXXXXX', 'XXX']                                                                                                                                           
['XXXXXXX', 'XXX', 'XXXXXXXXX']                                                                                                                              
['XXXXXXX']
