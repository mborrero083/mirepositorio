const BooksService = require('./books.service');

const fakeBooks = [
  {
    _id: 1,
    name: 'Harry Potter',
  }
];

const MongoLibStub = {
  getAll: () => [...fakeBooks],
  create: () => {},
};

jest.mock('../lib/mongo.lib', () => jest.fn().mockImplementation(() => MongoLibStub));

describe('Test for BooksService', () => {
  let service;
  beforeEach(() => {
    service = new BooksService();
  });
  describe('test for getBooks', () => {
    test('should return a list books', async () => {
      const books = await service.getBooks({});
      console.log(books);
      expect(books.length).toEqual(1);
    });
  });
});
