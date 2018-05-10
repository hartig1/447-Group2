setwd("C:/Users/Ryan/Downloads")
data = read.csv("15zpallagi.csv")
for(i in c(1:length(data[,1]))){
#for(i in data){
  if(data[i,3] == 0 || data[i,3] == 99999){
    data[i,3] = NA
  }
  if(data[i,2] == 'AK' || data[i,2] == 'HI'){
    data[i,2] = NA
  }
}
data = na.omit(data)
state = data.frame(165414)
for(i in c(1:length(data[,1]))){
    state['state'] = data[i,2]
}
state
