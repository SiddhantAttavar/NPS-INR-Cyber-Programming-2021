# Mark's Lizardish Translator

## Problem Statement: <br>
In his quest to dominate the human race, Mark Zuckerberg makes a new language. He calls it Lizardish. Here are some differences between Lizardish and English:

- The Lizardish alphabet has the same letters as the English one, but different in meaning. For example 'E' in Lizardish may mean 'F' in English. However this does not mean that 'F' in Lizardish must mean 'E' in English. Formally, the Lizardish alphabet is a permutation of the English alphabet. The permutation will be given to you.
- Lizardish also doesn’t use whitespace characters for separating words. Thus, instead of space (' ') they use underscore ('_'). Other punctuations, such as question mark ('?') or exclamation mark ('!') remain the same as in English.

Mark wants to start a new social media company where the main language of communication is Lizardish. He understands that humans may find Lizardish hard to comprehend at first, so he needs a program which translates from Lizardish to English.
Help Mark by making this translator.

## Constraints: <br>
- 1 &le; _T_ &le; 150
- M is a permutation of the English Alphabet
- Each string is non-empty
- Each string may contain only lowercase and uppercase letters, underscores and  the following punctuation symbols: dot, comma, exclaimation and question mark.

## Input Format: <br>
 - The first line of the input contains an integer _T_, denoting the number of strings to be translated, followed by the string _S_, which is the English translation of "abcdefghijklmnopqrstuvwxyz" in Lizardish. _T_ and _S_ are separated a space. 
 - Then _T_ lines of Lizardish strings follow, each of which you should translate.

## Output Format: <br>
 - For each test case, print the translation of the Lizardish sentence in English.

## Sample input: <br>
```
5 qwertyuiopasdfghjklzxcvbnm
Ph
Pcssi
Bpke_kdc_epclc_jcijsc_mihyo?
Epcf_kdc_liswhyo_EIED_hy_Vimcvpcn_Zkdvp_siyo_viyecle.
Ipp!
```

## Sample output: <br>
```
Hi
Hello
What are these people doing?
They are solving TOTR in Codechef March long contest.
Ohh!
```
