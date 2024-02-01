setwd("C:\\Users\\rravu\\Downloads\\Project 1")
data <- read.table("hate_crimes.csv", sep = ",", header = TRUE,
                  stringsAsFactors = FALSE)
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

# New Data Set

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

# Third Attempt
color_palette <- c("red", "blue", "green", "orange", "purple")

# Create a vector of colors that repeats every 5 bars
bar_colors <- rep(color_palette, each = 5)

# Apply the highlighting to the bar plot
col <- bar_colors

sorted_data <- subdat[order(subdat$avg_hatecrimes_per_100k_fbi, decreasing = TRUE), ]
Top_25_states = head(sorted_data, 25)
Top_25_states_desc <- sorted_data[order(-Top_25_states$avg_hatecrimes_per_100k_fbi),]
barplot(Top_25_states_desc$avg_hatecrimes_per_100k_fbi,
        names.arg = Top_25_states_desc$state,
        horiz = TRUE,
        las = 1,
        cex.names = 0.37, font = 2,
        ylab = 'Top 25 States with highest Hate Crime Rate', adj = 0.5,
        cex.lab = 0.85,
        font.lab = 4,
        col = col)

title(main = 'A look at Hate Crime Rates across the states (2010-2015)', adj = 0, font.main = 4)
title(xlab = "Avg Number of Hate Crimes Committed Per 100K Population", adj = 0.3, font.lab = 4)



