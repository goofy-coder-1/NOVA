# ================== LIST vs TUPLE vs SET ==================
#
# Brackets are NOT just decoration — they define behavior.
#
# List  -> [ ]
#   - Ordered
#   - Mutable (can change values)
#   - Allows duplicates
#
#   Example:
#   a = [1, 2, 3]
#   a[0] = 99   # works
#
# Tuple -> ( )
#   - Ordered
#   - Immutable (cannot change values)
#   - Allows duplicates
#
#   Example:
#   b = (1, 2, 3)
#   b[0] = 99   # -> error
#
# Set   -> { }
#   - Unordered
#   - Mutable
#   - NO duplicates
#   - No indexing
#
#   Example:
#   c = {1, 2, 3, 3}
#   print(c)    # {1, 2, 3}
#
# IMPORTANT:
#   {}      -> dictionary (NOT a set)
#   set()   -> empty set
#
# CONVERSION (explicit, not automatic):
#   list → tuple : tuple(my_list)
#   list → set   : set(my_list)
#   set  → list  : list(my_set)
#
# Mental model:
#   List  = editable notebook
#   Tuple = permanent record
#   Set   = no-duplicates bouncer
#
# ==========================================================
