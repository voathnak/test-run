__author__ = 'vlim'

## What is an Instance?

class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

#
#

## Using Classes

# from pets import Pet
polly = Pet("Polly", "Parrot")
print "Polly is a %s" % polly.getSpecies()
# Polly is a Parrot
print "Polly is a %s" % Pet.getSpecies(polly)
# Polly is a Parrot
# print "Polly is a %s" % Pet.getSpecies()
# Traceback (most recent call last):
#   File "", line 1, in
# TypeError: unbound method getSpecies() must be called with Pet instance as first
# argument (got nothing instead)

## Subclasses

class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

 # from pets import Pet, Dog
mister_pet = Pet("Mister", "Dog")
print 'Pet("Mister", "Dog"): %s' % mister_pet
mister_dog = Dog("Mister", True)
print 'Dog("Mister", True): %s' % mister_dog

print "isinstance(mister_pet, Pet): %s" % isinstance(mister_pet, Pet)
print "isinstance(mister_pet, Dog): %s" % isinstance(mister_pet, Dog)
print "isinstance(mister_dog, Pet): %s" % isinstance(mister_dog, Pet)
print "isinstance(mister_dog, Dog): %s" % isinstance(mister_dog, Dog)
