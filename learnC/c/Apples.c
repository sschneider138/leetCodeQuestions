#include <stdio.h>
#include <math.h>

int main()
{

    int appleQuantity;
    double applePrice = 1.49;
    double appleReview;
    int appleReviewDisplay;
    const char appleLocation = 'F';
    int numAppleReviewers;
    int daysOfWeek = 0;

    appleQuantity = 23;
    appleReview = 823;
    numAppleReviewers = 9;

    appleReview += 52;
    numAppleReviewers ++;

    appleReviewDisplay = round(appleReview / numAppleReviewers);

    while (daysOfWeek != 3)
    {
        printf("current day number: %d\n", daysOfWeek);
        daysOfWeek++;
    }
    if (appleQuantity < 10)
    {
        printf("Sale on apples today, today only they are: $%.2f\n", applePrice * .9);
    }
    else if (daysOfWeek == 3)
    {
        printf("Sale on apples today, today only they are: $%.2f\n", applePrice * .9);
    }

    // Put all your code above this and if you declare your variables using the given names and types there is no need to change any of the code below.
    printf("An apple costs: $%.2f, there are %d in inventory found in section: %c and your customers gave it an average review of %d%%!", applePrice, appleQuantity, appleLocation, appleReviewDisplay);
}