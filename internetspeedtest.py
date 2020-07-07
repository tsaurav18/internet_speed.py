from speedtest import Speedtest
st = Speedtest()
m = True
while(m){
print("download:", st.download())
print("upload:", st.upload())
}
st.get_servers([])
print("ping:", st.results.ping)
