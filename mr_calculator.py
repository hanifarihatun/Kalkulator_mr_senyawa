import streamlit as st
import pandas as pd

st.title('APLIKASI KALKULATOR MR SENYAWA')
st.write('Kelompok 7')
st.header('Apa itu massa molekul relatif?')
st.write('Massa molekul relatif adalah gabungan penjumlahan nilai massa atom relatif (Ar) dari atom-atom pembentuk molekul tersebut.')
st.write('Dengan ditemukannya cara menghitung massa molekul relatif ini, memudahkan para ilmuwan untuk mengetahui massa suatu molekul karena ukurannya yang sangat kecil sehingga tidak memungkinkan untuk dihitung menggunakan timbangan atau neraca.')
st.write('Selain massa atom relatif (Ar), kamu juga perlu memahami massa molekul relatif (Mr). Sebab, keduanya sering digunakan dalam perhitungan kimia.')
st.header('Bagaimana rumusnya? ')
st.write('Mr molekul AxBy = (x.Ar A)+(y.Ar B)+dst')
st.header('Ayo masukkan formulamu!')


def  calculate_mr(formula):
    elements = {}
    total_mass = 0
    
    # Membaca data Ar dari file CSV
    data = pd.read_csv('atomic_weights.csv')
    
    # Menghapus spasi dari kolom 'Symbol'
    data['Symbol'] = data['Symbol'].str.strip()
    
    # Menghitung molar mass dari setiap elemen dalam formula
    i = 0
    while i < len(formula):
        char = formula[i]
        if char.isupper():
            element = char
            # Jika elemen memiliki indeks lebih dari 1 dan huruf kedua adalah huruf kecil, contoh: Na, Fe
            if i + 1 < len(formula) and formula[i + 1].islower():
                element += formula[i + 1]
                i += 1
            
            count = 1
            # Jika elemen memiliki indeks atau angka lebih dari 1
            if i + 1 < len(formula) and formula[i + 1].isdigit():
                count = int(formula[i + 1])
                i += 1
            
            try:
                # Mengambil data Ar elemen dari CSV
                atomic_weight_str = data.loc[data['Symbol'] == element, 'Ar'].iloc[0]
                
                # Mengkonversi string ke float
                atomic_weight = float(atomic_weight_str.replace(',', '')) if isinstance(atomic_weight_str, str) else atomic_weight_str
                
                # Menghitung molar mass dari elemen
                molar_mass = atomic_weight * count
                
                elements[element] = molar_mass
                total_mass += molar_mass
            except IndexError:
                st.error(f"Elemen '{element}' tidak ditemukan dalam database.")
                return None, None, None  # Mengembalikan None untuk menunjukkan kegagalan
        
        i += 1
    
    # Jika tidak ada elemen yang ditemukan, kembalikan None
    if not elements:
        st.error("Tidak ada elemen yang ditemukan dalam formula.")
        return None, None, None
    
    # Menghitung persentase massa dari setiap elemen
    mass_percentage = {element: (mass / total_mass) * 100 for element, mass in elements.items()}

    return total_mass, elements, mass_percentage




# Main function
def main():
    st.write('')

formula = st.text_input('Masukkan formula senyawa, contoh: H2SO4, NaCl (Tuliskan tata nama senyawa sesuai standar IUPAC!!)')
    
if st.button('Hitung'):
    total_mass, elements, mass_percentage = calculate_mr(formula)
        
    # Output
    st.write("\nResult:")
    st.write(f"Molar mass : {total_mass:.5f}")
    st.write("Molar mass of elements :")
    for element, mass in elements.items():
        st.write(f"{element} : {mass:.5f}")
        
    st.write("Mass percentage :")
    for element, percentage in mass_percentage.items():
        st.write(f"{element} x {formula.count(element)} : {percentage:>{10}.7f}%")


if __name__ == '__main__':
    main()

st.write('Created by:')
st.write('Annisa Zahra S (2360074)')
st.write('Gea Aurelia (2360130)')
st.write('Hani Farihatun N (2360136)')
st.write('Lia Afriani (2360161)')




