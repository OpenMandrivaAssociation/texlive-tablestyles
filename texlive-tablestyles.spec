Name:		texlive-tablestyles
Version:	34495
Release:	2
Summary:	Styles for tables with new commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tablestyles
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablestyles.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablestyles.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablestyles.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package tries to introduce a separation of text and style
in tables by defining reusable table commands and a simple
interface to define a style for a table. Furthermore the
package defines commonly used column styles and a bugfix
command for lists in tables.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tablestyles
%{_texmfdistdir}/tex/latex/tablestyles
%doc %{_texmfdistdir}/doc/latex/tablestyles

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
