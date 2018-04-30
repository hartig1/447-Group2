setwd("C:/Users/ryanh/Documents/School/Software Engenering/447-I_am_root/Documentation and data")
data = read.csv("15zpallagi.csv")
for(i in c(1:length(data[,1]))){
  if(data[i,3] == 0 || data[i,3] == 99999){
    data[i,3] = NA
  }
  if(data[i,2] == 'AK' || data[i,2] == 'HI'){
    data[i,2] = NA
  }
}
data = na.omit(data)
i2 = 1
s = vector("list",length(data[,1])/6)
z = vector("list",length(data[,1])/6)
a = vector("list",length(data[,1])/6)
#for(i in c(1:as.integer(length(data[,1])))){
i=1
while(i<length(data[,1])){
    s[i2] = as.character(data[i,2])
    z[i2] = data[i,3]
    AGI = data[i,5] * 12500
    AGI = AGI + data[i+1,5] * 37500
    AGI = AGI + data[i+2,5] * 62500
    AGI = AGI + data[i+3,5] * 87500
    AGI = AGI + data[i+4,5] * 150000
    AGI = AGI + data[i+5,5] * 250000
    pop = data[i,5]
    pop = pop + data[i+1,5]
    pop = pop + data[i+2,5]
    pop = pop + data[i+3,5]
    pop = pop + data[i+4,5]
    pop = pop + data[i+5,5]
    a[i2] = as.integer(AGI/pop)
    i = i+6
    i2 = i2+1
}
income = data.frame(matrix(unlist(s)), matrix(unlist(z)),matrix(unlist(a)))
colnames(income)[1] = "state"
colnames(income)[2] = "zip"
colnames(income)[3] = "agi"
write.csv(income,"AGI.csv")
