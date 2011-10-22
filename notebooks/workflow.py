# <nbformat>2</nbformat>

# <markdowncell>

# # Python workflow for scientific computing
# 
# ## Executing simple statements
# 
# * Python as a simple calculator
# * Defining variables and printing their content

# <codecell>
x = 2

# <markdowncell>

# ## Understanding objects
# * The tab key
# * Builtin help with `x?` and `x??`

# <codecell>
s = 'Hello Claremont'

# <markdowncell>
#
# ## Understanding the notebook and saving your work
# * Text vs code cells
# * Execution of code, output
# * The panel on the left
# * Saving your notebooks
# * Basic [Markdown text](http://daringfireball.com/markdown/syntax)
# * Using Mathematics in the text cells
# * Embedding images and videos

# <markdowncell>

# ## More complex code
# * Multiline statements (if, for)
# * Defining  a simple function
# * Calling a function

# <codecell>
for i in range(10):
    print i**2,

# <markdowncell>
#
# ## Making a figure

# <codecell>

hist(randn(5000), bins=50)

# <markdowncell>

# ## Finding help 
# 
# * The Python documentation
# * The docs for related projects (links on the left)

# <markdowncell>

# ## Understanding error messages

# <codecell>
1/0

# <markdowncell>
#
# ## Files on your computer and access to the operating system
# * pwd, cd, ls
# * %run
# * !commands
# * loading a simple data file from disk

# <codecell>

