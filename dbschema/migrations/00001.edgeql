CREATE MIGRATION m177fjldrpp5jrjt22avczjhw7u7lvncpuwgpel56bk6gpyzrny5ia
    ONTO initial
{
  CREATE TYPE default::Post {
      CREATE REQUIRED PROPERTY author: std::str;
      CREATE MULTI PROPERTY comments: std::str;
      CREATE REQUIRED PROPERTY content: std::str;
      CREATE REQUIRED PROPERTY title: std::str;
  };
};
