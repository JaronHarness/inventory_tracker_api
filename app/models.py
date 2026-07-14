from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, func, Text, Numeric
from sqlalchemy.orm import relationship

class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(20), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    unit_cost = Column(Numeric(10,2))
    unit_of_measure = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now())

    # Foreign Keys:
    category_id = Column(Integer, ForeignKey('categories.id'), index=True, nullable=False)

    # Relationships:
    category = relationship('Category', back_populates='items')
    stock_levels = relationship('StockLevels', back_populates='item')


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now())

    # Relationships:
    items = relationship('Items', back_populates='category')

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    location_type = Column(String(50))
    address = Column(String(200))
    description= Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now())

    # Relationships:
    stock_levels = relationship('StockLevels', back_populates='location')

class StockLevels(Base):
    __tablename__ = 'stock_levels'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    minimum_quantity_threshold = Column(Integer, default=0)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now())

    # Foreign Keys:
    location_id = Column(Integer, ForeignKey('locations.id'), index=True, nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), index=True, nullable=False)

    # Relationships:
    item = relationship('Items', back_populates='stock_levels')
    location = relationship('Location', back_populates='stock_levels')
