# Whoknows

Seek and you shall find.

## Usage

Search through a repository and find out who's modified code containing a keyword/phrase (hereby referred to as `keyphrase`).

## Dependencies

* [python](https://www.python.org)

## Installation

```bash
git clone https://github.com/cuzzo/whoknows.git
```

All the cool kids are aliasing `whoknows` to `gwk`. You should, too.

```bash
alias gwk=$(pwd)/whoknows/whoknows
```

Aliases go away when you restart your computer. You can add it to your `.bashrc` to fix that.

```bash
echo "alias gwk=$(pwd)/whoknows/whoknows" >> ~/.bashrc
```

## Examples

```bash
$ whoknows lemma
> Cuzzo: 30
> Suzy: 4
> Mony: 1
```

```bash
$ whoknows lemma in/some/subdir
> Cuzzo: 21
> Suzy: 1
```

## Options

`-a` search through all files containing the keyphrase, and report any line in that file--whether it contains the keyphrase or not.

This differs from the default behavior in that only lines which contain the keyphrase are reported. `-a` can be useful when you want to know who is modifying code *around* a keyphrase, and not just who is modifying code that *contains* the keyphrase. Therefore, the usefullness of `-a` approaches 0 extremely quickly as the line numbers in your files approaches infinity [=

## Extra

### Get Top N Contributors
```bash
whoknows lemma | head -3
```

## Disclaimer

whoknows only reports the *most recent* contributers who have modified a line containing a keyphrase. It does not look for all contributers who have ever modified a line containing a keyphrase; nor does it look for the contributers who initially authored a line containing a keyphrase.

Pull requests to add these features would be greatly appreciated and quickly accepted [=

## License

whoknows is free--as in BSD. Hack you heart out, hackers.
