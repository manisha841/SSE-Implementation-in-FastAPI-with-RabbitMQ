module default {
  type Blog {
    required title: str;
    required content: str;
    required author: str;
    multi comments: str;
  }
}