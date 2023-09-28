import streamlit as st
import plotly.express as px
import pandas as pd
import itertools 
from PIL import Image


def main_menu():
    option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Pencarian Data','Tampilkan Data','Urutkan Data')
    )
    if option == 'Home' or option == '':
        st.write("""# PROGRAM STATITISKA KEMISKINAN DI PULAU JAWA""") #menampilkan halaman utama
        image = Image.open('pulau jawa.jpg')
        st.image(image, width=600)
    elif option == 'Pencarian Data':
        st.write("""## Pencarian Data""")
        search_list = st.text_input("Masukan Nama Daerah Yang Ingin Di Cari: ")
        search_result = search(data_semua, search_list)
        df_data = pd.DataFrame(search_result, columns=['Kabupaten/Kota', 'Data'])
        st.write(df_data)
        st.write("\n")
    elif option == 'Tampilkan Data':
        st.write("""## Tampilkan Data""")
        show_data()
    elif option == 'Urutkan Data':
        st.write("""## Urutkan Data""")
        sort_data()
        
def show_data():
        st.write("""### Silahkan Pilih : """)
        st.write("1. Jawa Tengah")
        st.write("2. Jawa Timur")
        st.write("3. Jawa Barat")
        st.write("4. Tampilkan Seluruh Data")
        pilih = st.text_input("Masukan pilihan Anda (1-4): ")
        if pilih == "1":
            st.write("Data Jawa Tengah")
            df_data = pd.DataFrame(data_jateng, columns=['Kabupaten/Kota', 'Data'])
            st.write(df_data)
            st.write("\n")
        elif pilih == "2":
            st.write("Data Jawa Timur")
            df_data = pd.DataFrame(data_jatim, columns=['Kabupaten/Kota', 'Data'])
            st.write(df_data)
            st.write("\n")
        elif pilih == "3":
            st.write("Data Jawa Barat")
            df_data = pd.DataFrame(data_jabar, columns=['Kabupaten/Kota', 'Data'])
            st.write(df_data)
            st.write("\n")
        elif pilih == "4":
            data_jatengfx = list(data_jateng) 
            data_jatimfx = list(data_jatim) #mengubah data dictionary() menjadi list()
            data_jabarfx = list(data_jabar) 
            #menggabungkan 3 data dengan iteratool.chain()
            data = itertools.chain(data_jatengfx, data_jatimfx, data_jabarfx)
            st.write("Data 3 Provinsi")
            df_data = pd.DataFrame(data, columns=['Kabupaten/Kota', 'Data'])
            st.write(df_data)
        else:
            st.write("Pilihan tidak valid. Silahkan coba lagi.")
        st.write("\n")
            
def sort_data():
        st.write("""### Silahkan Pilih : """)
        st.write("1. Jawa Tengah")
        st.write("2. Jawa Timur")
        st.write("3. Jawa Barat")
        st.write("4. 3 Provinsi")
        pilih = st.text_input("Masukan pilihan Anda (1-4): ")
        if pilih == "1":
            st.write("""## Jawa Tengah""")
            sort_jateng = sort(data_jateng)
            chart(sort_jateng)
            st.write("\n")
        elif pilih == "2":
            st.write("""## Jawa Timur""")
            sort_jatim = sort(data_jatim)
            chart(sort_jatim)
            st.write("\n")
        elif pilih == "3":
            st.write("""## Jawa Barat""")
            sort_jabar = sort(data_jabar)
            chart(sort_jabar)
            st.write("\n")
        elif pilih == "4":
            sort_data_all()
            st.write("\n")
        else:
            st.write("Pilihan tidak valid. Silahkan coba lagi.")
        st.write("\n")


#semua data
data_jateng = [("Kebumen", 17.83), ("Wonosobo", 17.67), 
                ("Brebes", 17.43), ("Pemalang", 16.65),
                ("Purbalingga", 16.24), ("Banjarnegara", 16.23), 
                ("Rembang", 15.8), ("Sragen", 13.83),
                ("Banyumas", 13.66), ("Klaten", 13.49)]

data_jatim = [("Sampang", 23.76), ("Bangkalan", 21.57), 
                ("Sumenep", 20.51), ("Probolinggo", 18.91),
                ("Tuban", 16.31), ("Ngawi", 15.57), 
                ("Pamekasan", 15.3), ("Pacitan", 15.11),
                ("Bondowoso", 14.73), ("Lamongan", 13.38)]

data_jabar = [("Kota Tasikmalaya", 13.13), ("Kuningan", 13.1), 
                ("Indramayu", 13.4), ("Majalengka", 12.33), 
                ("Cirebon", 12.3), ("Bandung Barat", 11.3),
                ("Cianjur", 11.18), ("Tasikmalaya", 14.15),
                ("Sumedang", 10.71), ("Garut", 10.6)]
    
data_semua = [("Kebumen", 17.83), ("Wonosobo", 17.67), 
                ("Brebes", 17.43), ("Pemalang", 16.65),
                ("Purbalingga", 16.24), ("Banjarnegara", 16.23), 
                ("Rembang", 15.8), ("Sragen", 13.83),
                ("Banyumas", 13.66), ("Klaten", 13.49),
                ("Sampang", 23.76), ("Bangkalan", 21.57), 
                ("Sumenep", 20.51), ("Probolinggo", 18.91),
                ("Tuban", 16.31), ("Ngawi", 15.57), 
                ("Pamekasan", 15.3), ("Pacitan", 15.11),
                ("Bondowoso", 14.73), ("Lamongan", 13.38),
                ("Kota Tasikmalaya", 13.13), ("Kuningan", 13.1), 
                ("Indramayu", 13.4), ("Majalengka", 12.33), 
                ("Cirebon", 12.3), ("Bandung Barat", 11.3),
                ("Cianjur", 11.18), ("Tasikmalaya", 14.15),
                ("Sumedang", 10.71), ("Garut", 10.6)]

def sort_data_all():
    data_jatengfx = list(data_jateng) 
    data_jatimfx = list(data_jatim) #mengubah data dictionary() menjadi list()
    data_jabarfx = list(data_jabar) 

    #menggabungkan 3 data dengan iteratool.chain()
    data = itertools.chain(data_jatengfx, data_jatimfx, data_jabarfx)

    #mengurutkan data dari Descending
    data = sorted(data, key=lambda x:x[1], reverse=True)

    #perulangan untuk menampilkan data dari atas kebawah
    st.write("Urutan Kota Termiskin di Pulau Jawa")
    chart(data)

def sort(data):
    return sorted(data, key=lambda x: x[1])

def chart(data):
    df_data = pd.DataFrame(data, columns=['Kabupaten/Kota', 'Data'])
    st.bar_chart(df_data, x='Kabupaten/Kota', y='Data')

def search(list,x):
    i = []
    for item in list:
        if x.lower() in item[0].lower():
            i.append(item)
            return i

main_menu()