# Test Page for formatting option for FlyByWire documentation

``` md title="Headers"
{
# H1
## H2
### H3
#### H4
##### H5
###### H6
}
```

# H1
## H2
### H3
#### H4
##### H5
###### H6

---

``` md title="Normal Text"
**Bold** __Bold__

^^Underline^^

*Italics* _Italics_

Super^script^

Sub~script~

\==highlighted background== (remove backslash)

\~~red highlighted background~~ (remove backslash)

\{\== (remove backslash)

highlighted background box

==}

\{\-- (remove backslash)

red highlighted background box

--}
```
**Bold** __Bold__

^^Underline^^

*Italics* _Italics_

Super^script^

Sub~script~

==highlighted background==

~~red highlighted background~~

{==

highlighted background box

==}

{--

red highlighted background box

--}

___

``` md title="Include (INOP)"
--8<-- "./docs/test_include.md"
```

Here should follow an included file:

--8<-- "./docs/test_include.md"

---

``` md title="Include (INOP)"
!!! info "Info box"
    Test of info box

!!! info ""
    Test of info box with empty title

!!! warning "Warning box"
    Test of warning box

!!! warning ""
    Test of warning box with empty title

??? "Collapsible box"
    Test of box

??? info "Collapsible Info box"
    Test of info box

??? warning "Collapsible Warning box"
    Test of warning box
```

!!! info "Info box"
    Test of info box

!!! info ""
    Test of info box with empty title

!!! warning "Warning box"
    Test of warning box

!!! warning ""
    Test of warning box with empty title

??? "Collapsible box"
    Test of box

??? info "Collapsible Info box"
    Test of info box

??? warning "Collapsible Warning box"
    Test of warning box

Find more admonitions here: [https://squidfunk.github.io/mkdocs-material/reference/admonitions/](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

---




---

| Col 1 | Col 2 |
|:------|:------|
| 123   | 456   |

`Monospaced`

Keyboard shortcuts: ++ctrl+f5++

```
// code
h3 {
  color: #00C2CB;
}
```

[This is a link to the first headline](#h1)

[This is an external link](https://flybywiresim.com/)


Full size logo

![Logo Image full size](assets/images/FBW-Tail.png)

20% sized responsive logo

![Logo Image Small](assets/images/FBW-Tail.png){ width=20% }

---

!!! block "Aligned images"
    ![Logo Image Small aligned left](assets/images/FBW-Tail.png){ width=30% align=left}

    ![Logo Image Small aligned right](assets/images/FBW-Tail.png){ width=30% align=right}

---

=== "Tab 1"
    This is tab 1

=== "Tab 2"
    This is tab 2

[Download Button](assets/FBW_A32NX_CHECKLIST.pdf){ .md-button }





