### Basics

**Hash table syntax:** `@{ <name> = <value>; [<name> = <value> ] ...}`
- **@** begins hash table
- **{** hash table **}**
- **;** separates key-value pairs (or line break)
- **=** between key and value (key = value)
- **"** key containing spaces **"**, **"** string_value **"**
- **\[ordered]** before @ specifies the order of the table matters

*Example*
```PowerShell
$hash = @{
    1       = 'one'
    2       = 'two'
    'three' = 3
}
$hash
```

Common properties:
- **.Count**: \# key-value pairs
- **.Keys**: returns all keys
- **.Values**: returns all values
- **.Item**: returns value for the key (`$hash.1`returns `"one"` in the above example), values can also be accessed using an index syntax (`$hash['three']` returns `3`)

### Iterating

*All these methods can be used to accomplish the same result:*

```Powershell
foreach ($Key in $hash.Keys) {
    "The value of '$Key' is: $($hash[$Key])"
}
```

```Powershell
$hash.Keys | ForEach-Object {
    "The value of '$_' is: $($hash[$_])"
}
```

```Powershell
$hash.GetEnumerator() | ForEach-Object {
    "The value of '$($_.Key)' is: $($_.Value)"
}
```

```Powershell
$hash.GetEnumerator().ForEach({"The value of '$($_.Key)' is: $($_.Value)"})
```

### Adding

```powershell
$hash[new_key] = new_value
```

```powershell
$hash.Add(new_key, new_value)
```

```powershell
$hash = $hash + @{ new_key = new_value }
```

### Removing

```powershell
$object.Remove(key)
```


LEARN MORE: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_hash_tables