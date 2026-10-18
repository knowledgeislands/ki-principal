#!/usr/bin/perl
# rewrite-links.pl MAP IDS FILE: print FILE with every citation of a moved path rewritten, for 06-citations.sh.
#
# MAP holds the old and new repository-relative path of each move, tab separated; IDS the old thread stem and new
# work id of each moved work. A path matches a move exactly or lies under it; one under a moved folder is rewritten
# only when it exists at either end, so a link to a report deleted before the migration is left and reported dead.
# Four forms are rewritten: relative Markdown links, resolved from FILE's folder and recomputed from FILE's folder
# after the move; paths after `ki-principal/`, which covers absolute paths; repository-relative paths in backticks or
# quotes; and old thread stems in backticks. Each dead link is reported on stderr.

use strict;
use warnings;
use File::Basename qw(dirname);
use File::Spec;

my ($map_file, $ids_file, $file) = @ARGV;
my (@moves, %ids);
open my $map, '<', $map_file or die "$map_file: $!";
while (<$map>) { chomp; my ($old, $new) = split /\t/; push @moves, [$old, $new] if $old && $new }
@moves = sort { length $b->[0] <=> length $a->[0] } @moves;
open my $idf, '<', $ids_file or die "$ids_file: $!";
while (<$idf>) { chomp; my ($stem, $id) = split /\t/; $ids{$stem} = $id if $stem && $id }

# moved PATH: the new path, '' when PATH has not moved, or undef when it lies under a move but exists at neither end.
sub moved {
  my ($path) = @_;
  for my $move (@moves) {
    my ($old, $new) = @$move;
    return $new if $path eq $old;
    if (index($path, "$old/") == 0) {
      my $to = $new . substr($path, length $old);
      return (-e $path || -e $to) ? $to : undef;
    }
  }
  return '';
}

sub normal {
  my @parts;
  for (split m{/}, $_[0]) { next if $_ eq '' || $_ eq '.'; if ($_ eq '..') { pop @parts } else { push @parts, $_ } }
  return join '/', @parts;
}

my $from = dirname($file);
my $self = moved($file);
my $to = dirname($self ? $self : $file);

sub relative_link {
  my ($open, $target, $tail, $close) = @_;
  return undef if $target =~ m{^(?:[a-z][a-z0-9+.-]*:|/|#)}i;
  my $path = normal("$from/$target");
  my $new = moved($path);
  if (!defined $new) { print STDERR "dead link in $file: $target\n"; return undef }
  return undef if $new eq '' && $to eq $from;
  my $relative = File::Spec->abs2rel($new eq '' ? $path : $new, $to);
  return "$open$relative$tail$close";
}

my $text = do { local $/; open my $in, '<', $file or die "$file: $!"; <$in> };

$text =~ s{(\]\(<?)([^)>#\s]+)(#[^)>\s]*)?(>?\))}{ relative_link($1, $2, $3 // '', $4) // $& }ge;

sub cited_path {
  my ($whole, $lead, $path) = @_;
  my $new = moved($path);
  if (!defined $new) { print STDERR "dead path in $file: $path\n"; return $whole }
  return $new eq '' ? $whole : "$lead$new";
}

for my $move (@moves) {
  my $pattern = quotemeta $move->[0];
  $text =~ s{(ki-principal/|(?<=[`"'\s(]))($pattern(?:/[^\s`"')>\]]*[^\s`"')>\].,:;])?/?)(?=[`"'\s)>\]#:,.]|$)}{ cited_path($&, $1, $2) }gem;
}

for my $stem (sort { length $b <=> length $a } keys %ids) {
  my $pattern = quotemeta $stem;
  $text =~ s{`$pattern`}{`$ids{$stem}`}g;
}

print $text;
