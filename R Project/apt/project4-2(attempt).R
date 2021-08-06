# 2. 1호선 역곡역 / 경기도 부천시 아파트 실거래 정보

# 경기 부천시 역곡로 1 (역곡역 1호선) 역곡동 382

# guro_map <- get_googlemap("gurogu", maptype="roadmap", zoom=12)
# ggmap(guro_map)
# onsu_map <- get_googlemap("onsu station", maptype = "roadmap", zoom=15)

Sys.setlocale("LC_ALL","korean")
install.packages("dplyr")
library(dplyr)
install.packages("devtools")
library(devtools)
install_github("dkahle/ggmap")
library(ggmap)

googleAPIkey <- "AIzaSyDZMHAc6CwmHiyZcU9BQodtSS4n42WZwKY"
register_google(googleAPIkey)


# 3. 아파트 실거래가 데이터 가공하기
#전용면적별 거래 가격
apt_data <- read.csv("아파트_실거래가_부천.csv")
head(apt_data)

apt_data$전용면적 = round(apt_data$전용면적)
head(apt_data)

count(apt_data, 전용면적) %>% arrange(desc(n))

apt_data_85 <- subset(apt_data, 전용면적=="85")
head(apt_data_85)


# 아파트 단지별 평균 거래 금액
apt_data_85$거래금액 <- gsub(",","", apt_data_85$거래금액)
head(apt_data_85)

apt_data_85_cost <- aggregate(as.integer(거래금액)~ 단지명, apt_data_85, mean)
head(apt_data_85_cost)

apt_data_85_cost <- rename(apt_data_85_cost, "거래금액" = "as.integer(거래금액)")
head(apt_data_85_cost)

apt_data_85 <- apt_data_85[!duplicated(apt_data_85$단지명),]
head(apt_data_85)

apt_data_85 <- left_join(apt_data_85, apt_data_85_cost, by = "단지명")
head(apt_data_85)

apt_data_85 <- apt_data_85%>% select("단지명","시군구","번지","전용면적","거래금액.y")
apt_data_85 <- rename(apt_data_85, "거래금액" = "거래금액.y")
head(apt_data_85)


# 시군구와 번지를 하나로 합치기
apt_address <- paste(apt_data_85$"시군구", apt_data_85$"번지")
head(apt_address)

apt_address <- paste(apt_data_85$"시군구", apt_data_85$"번지") %>% data.frame()
head(apt_address)

apt_address <- rename(apt_address, "주소" = ".")
head(apt_address)


#좌표 정보 추가 후 최종 데이터 만들기
apt_address_code <- as.character(apt_address$"주소")%>% enc2utf8() %>% geocode()

apt_code_final <- cbind(apt_data_85, apt_address, apt_address_code) %>% 
  select("단지명","전용면적","거래금액","주소", lon, lat)
head(apt_code_final)




# 4. 구글 지도에 지하철역과 아파트 가격 표시하기
# 부천 지도 가져오기
bucheon_map <- get_googlemap("bucheon", maptype = "roadmap", zoom=12)
ggmap(bucheon_map)

# 지하철역 위치 및 아파트 가격 정보 표시하기
yeokgok_map <- get_googlemap("yeokgok station", maptype = "roadmap", zoom=15)
ggmap(yeokgok_map)

ggmap(yeokgok_map) +
  geom_point(data = apt_code_final, aes(x = lon, y = lat)) +
  geom_text(data = apt_code_final, aes(label = 단지명, vjust = -1)) +
  geom_text(data = apt_code_final, aes(label = 거래금액, vjust = 1))
