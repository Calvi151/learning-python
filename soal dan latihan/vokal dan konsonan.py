def mengecek_huruf(huruf):
    huruf = huruf.upper()
    
    huruf_vokal ="AIUEO"
    if  huruf.isalpha() and  len(huruf) == 1:
        if huruf in huruf_vokal:
            return "Hurufmu Vokal"
        else:
            return "Hurufmu Konsonan" 
    else:
         "yang kamu masukan bukan huruf"
         
input = input('Masukan huruf dari A-Z:\t')
hasilnya= mengecek_huruf(input) 
print(hasilnya)        
    