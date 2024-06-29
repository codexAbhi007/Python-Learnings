# Logging

Logging is a means of tracking events that happen when some software runs. Logging is important for software developing, debugging, and running. If you don’t have any logging record and your program crashes, there are very few chances that you detect the cause of the problem. And if you detect the cause, it will consume a lot of time. With logging, you can leave a trail of breadcrumbs so that if something goes wrong, we can determine the cause of the problem.

There are a number of situations like if you are expecting an integer, you have been given a float and you can a cloud API, the service is down for maintenance, and much more. Such problems are out of control and are hard to determine.

## Why print statement is not Pythonic

Some developers use the concept of printing the statements to validate if the statements are executed correctly or if some error has occurred. But printing is not a good idea. It may solve your issues for simple scripts but for complex scripts, the printing approach will fail.
Python has a built-in module logging which allows writing status messages to a file or any other output streams. The file can contain information on which part of the code is executed and what problems have arisen.

## Python Logging Levels

There are five built-in levels of the log message.  

- **Debug**: These are used to give Detailed information, typically of interest only when diagnosing problems.
- **Info**: These are used to confirm that things are working as expected
- **Warning**: These are used as an indication that something unexpected happened, or is indicative of some problem in the near future
- **Error**: This tells that due to a more serious problem, the software has not been able to perform some function
- **Critical**: This tells serious error, indicating that the program itself may be unable to continue running

If required, developers have the option to create more levels but these are sufficient enough to handle every possible situation. Each built-in level has been assigned its numeric value.

|LEVEL|Numeric Value|
|-----|-------------|
|NOTSET|0 |
|DEBUG |10|
|INFO |20|
|WARNING |30|
|ERROR |40|
|CRITICAL |50|

The logging module is packed with several features. It has several constants, classes, and methods. The items with all caps are constant, the capitalized items are classes and the items which start with lowercase letters are methods. 

There are several logger objects offered by the base Handler itself.  

- Logger.info(msg): This will log a message with level INFO on this logger.
- Logger.warning(msg): This will log a message with a level WARNING on this logger.
- Logger.error(msg): This will log a message with level ERROR on this logger.
- Logger.critical(msg): This will log a message with level CRITICAL on this logger.
- Logger.log(lvl,msg): This will Log a message with integer level lvl on this logger.
- Logger.exception(msg): This will log a message with level ERROR on this logger.
- Logger.setLevel(lvl): This function sets the threshold of this logger to lvl. This means that all the messages below this level will be ignored.
- Logger.addFilter(filt): This adds a specific filter fit into this logger.
- Logger.removeFilter(filt): This removes a specific filter fit into this logger.
- Logger.filter(record): This method applies the logger’s filter to the record provided and returns True if the record is to be processed. Else, it will return False.
- Logger.addHandler(hdlr): This adds a specific handler hdlr to this logger.
- Logger.removeHandler(hdlr) : This removes a specific handler hdlr into this logger.
- Logger.hasHandlers(): This checks if the logger has any handler configured or not. 