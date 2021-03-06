#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

# long string
text_indentation('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres.')

# multiple spaces at end and beginning of newline
text_indentation('hi.      how   ?  you:    Lisa')

# prefix spaces
text_indentation('     <- spaces anyone?')

# all ......
text_indentation('.......')

# newlines without substitutions
text_indentation('hi  \n  how  \n  <- spaces anyone?->  \n  you:  Bobby?')

# non string
text_indentation(45)

# no punctuation marks
text_indentation("there is no punctuation here")

# no args
text_indentation()

# too many args
text_indentation("this", "that")

# input of None
text_indentation(None)

# input of bool
text_indentation(True)

# block of text
text_indentation('Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?" \n So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.')
