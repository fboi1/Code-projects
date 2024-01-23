library(haven)
data <- data.frame(natsal_3_teaching_open$sexidr, natsal_3_teaching_open$religimp)
data2 <- data.frame(natsal_3_teaching_open$rsex, natsal_3_teaching_open$depscr)
# Create contingency table
table <- table(data$natsal_3_teaching_open.sexidr, data$natsal_3_teaching_open.religimp)
table2 <- table(data2$natsal_3_teaching_open.rsex, data2$natsal_3_teaching_open.depscr)
# Conduct chi-squared test
chisq.test(table)
table
chisq.test(data$natsal_3_teaching_open.sexidr, data$natsal_3_teaching_open.religimp)

natsal_3_teaching_open$religimp
natsal_3_teaching_open$sexidr
nrow(natsal_3_teaching_open)
table
boxplot(natsal_3_teaching_open$sexidr, natsal_3_teaching_open$religimp)

fisher.test(table, simulate.p.value = TRUE)
###

table
chisq.test(table)
table <- table[-3, ]
table
#create 2x2 dataset
data3 = matrix(c(534, 913, 1069, 1126, 13, 22, 31, 68), nrow = 2, byrow = TRUE)
data3
chisq.test(data3)

#prop.table() function in R to calculate the proportions of the contingency table. To get the proportions by row, you can set the margin argument to 1.
prop.table(table, margin = 1)