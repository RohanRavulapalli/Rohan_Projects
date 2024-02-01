# Rohan Ravulapalli - Virginia Tech - Analyzing Annual Hate Crimes per 100K across States.

setwd("C:\\Users\\rravu\\Downloads\\Project 1")
data <- read.table("hate_crimes.csv", sep = ",", header = TRUE,
                  stringsAsFactors = FALSE)

# 1. Plotting a Standard Bar plot:

library('viridis')
num_bars1 <- 50
bar_colors1 <- viridis(num_bars1)

data <- data[!is.na(data$avg_hatecrimes_per_100k_fbi), ] #filters out rows with "N/A"
barplot(data$avg_hatecrimes_per_100k_fbi,
        names.arg = data$state, cex.names = 0.50, col = bar_colors1,
        ylab = "Avg annual hate crimes per 100k",
        las = 2,
        font.lab = 4)
title(main = 'A Look at Hate Crime Rates across the 50 states (2010-2015)', adj = 0,
      sub = "50 states", adj = 0.5, font.main = 4, font.sub = 4)

# 2. Plotting a Horizontal Variation of the Bar plot with only the top 25 states that possess the highest hate crime rates per 100k
# being included

subdat <- data[, c(1,12)]
subdat <- data.frame(subdat)
subdat_desc <- subdat[order(-subdat$avg_hatecrimes_per_100k_fbi),]
barplot(subdat_desc$avg_hatecrimes_per_100k_fbi,
        names.arg = subdat_desc$state,
        horiz = TRUE,
        las = 1,
        cex.names = 0.33,
        ylab = 'States', adj = 0.5,
        cex.lab = 0.8,
        font.lab = 4)
title(main = 'A look at Hate Crime Rates across the 50 states (2010-2015)', adj = 0, font.main = 4)
title(sub = 'Avg annual hate crimes commited per 100k', adj = 0.5, font.sub = 4)

# Outputs:

"C:\Users\rravu\Pictures\Screenshots\Screenshot 2024-01-31 194249.png" 
"C:\Users\rravu\Pictures\Screenshots\Screenshot 2024-01-31 194358.png"
