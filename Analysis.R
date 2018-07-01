#==================================================#
#========= pre-registered analysis script =========#
#==================================================#
# By Courtney Hilton, June, 2018

#==================================================#
#============== data and packages =================#
#==================================================#
if(!require(dplyr)){install.packages('dplyr')}
if(!require(ggplot2)){install.packages('ggplot2')}
library(dplyr)
library(ggplot2)
setwd("Documents/GitHub/Congruency_Music_Language/data")

# eventually iterate through all datasets here with for loop

trial_data <- read.delim("004trial_log.txt", sep = "\t", header = TRUE)

trial_data$Sentence <- as.character(trial_data$Sentence)
trial_data$Probe <- as.character(trial_data$Probe)
trial_data$Accuracy<- as.numeric(trial_data$Accuracy)


obj_rc <- trial_data %>%
    filter(Sentence_extraction == "object extracted", Probe_clause == "main_clause") %>%
    arrange(RT)

obj_rc_incongruent <- trial_data %>%
  filter(Sentence_extraction == "object extracted", Probe_clause == "main_clause", Congruency == "incongruent") %>%
  arrange(RT)

obj_rc_congruent <- trial_data %>%
  filter(Sentence_extraction == "object extracted", Probe_clause == "main_clause", Congruency == "congruent") %>%
  arrange(RT)



obj_rc_incongruent_RT <- mean(obj_rc_incongruent$RT)
obj_rc_incongruent_acc <- sum(obj_rc_incongruent$Accuracy) / length(obj_rc_incongruent$Accuracy)
obj_rc_congruent_RT <- mean(obj_rc_congruent$RT)
obj_rc_congruent_acc <- sum(obj_rc_congruent$Accuracy) / length(obj_rc_congruent$Accuracy)

#==================================================#
#============ Calculating stats etc ===============#
#==================================================#