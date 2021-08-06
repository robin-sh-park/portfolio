Sys.setlocale("LC_ALL","korean")
install.packages("readxl")
install.packages("dplyr")


library(readxl)
finedust <- read_excel("C:/Rstudy/finedust.xlsx")


View(finedust)
str(finedust)


library(dplyr)
finedust_analysis <- finedust %>% filter(area %in% c("구로구", "금천구"))
View(finedust_analysis)


count(finedust_analysis, yyyymmdd) %>% arrange(desc(n))
count(finedust_analysis, area) %>% arrange(desc(n))


dust_analysis_guro <- subset(finedust_analysis, area=="구로구")
dust_analysis_geumchon <- subset(finedust_analysis, area=="금천구")

dust_analysis_guro
dust_analysis_geumchon


install.packages("psych")
library(psych)
describe(dust_analysis_guro$finedust)
describe(dust_analysis_geumchon$finedust)


boxplot(dust_analysis_guro$finedust, dust_analysis_geumchon$finedust,
        main="구로구와 금천구의 미세먼지 농도 차이가 나는가?", xlab="AREA",
        names=c("구로구","금천구"), ylab="FINEDUST_PM", 
        col = c("orange","yellow"))

t.test(data = finedust_analysis, finedust ~ area, var.equal = T)
