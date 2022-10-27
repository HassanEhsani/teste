def ins_in_list ( arr , x ) :
     if  len ( arr ) == 0 :
        arr = [ x ] 
    elif x <= arr [ 0 ] :
        arr. insert ( 0 , x ) 
    elif x >= arr [ - 1 ] :
        arr. append ( x ) 
    else :
        a = 0 
        b = len ( arr ) 
        while  ( ba > 1 ) :
            c = ( a+b ) // 2 
            if x > arr [ c ] :
                a = c
             else :
                b = c
        arr. insert ( b , x ) 
    return arr    
 
_ = input ( )
 
arr = [ ] 
for x in  iter ( input ( ) . split ( ) ) ) :
    arr = ins_in_list ( arr , int ( x ) ) 
print ( arr )